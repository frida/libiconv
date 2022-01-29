project('libiconv', 'c', version: '1.17')

cc = meson.get_compiler('c')
sh = find_program('sh')
gperf = find_program('gperf')

libcharset_version = run_command('build-aux' / 'genversion.py', '1:0:0', host_machine.system(),
  capture: true,
  check: true,
).stdout().strip()
libiconv_version = run_command('build-aux' / 'genversion.py', '8:1:6', host_machine.system(),
  capture: true,
  check: true,
).stdout().strip()

# Suppress all compiler warnings when we're a subproject.
if meson.is_subproject() and cc.get_argument_syntax() != 'msvc'
  add_project_arguments('-w', language: 'c')
endif

cdata = configuration_data()

cdata.set('DLL_VARIABLE', '')

if host_machine.endian() == 'little'
  cdata.set('WORDS_LITTLEENDIAN', 1)
endif

extension_enablers = import('fs').read('extension-enablers.h')
cdata.set('EILSEQ', cc.compute_int('EILSEQ',
                                   prefix: '\n'.join([extension_enablers, '#include <errno.h>'])))

if cc.has_function('iconv')
  iconv_nonconst = cc.compiles('''
      #include <stdlib.h>
      #include <iconv.h>
      size_t iconv (iconv_t cd, char * *inbuf, size_t *inbytesleft, char * *outbuf, size_t *outbytesleft);
      ''',
      name: 'libc iconv() is compatible with its POSIX signature')
else
  # When compiling GNU libiconv on a system that does not have iconv yet,
  # pick the POSIX compliant declaration without 'const'.
  iconv_nonconst = true
endif
cdata.set('ICONV_CONST', iconv_nonconst ? '' : 'const')

cdata.set10('HAVE_WCHAR_T', cc.has_type('wchar_t', prefix: '#include <stddef.h>'))

foreach f : ['getc_unlocked', 'mbrtowc', 'wcrtomb', 'mbsinit', 'setlocale']
  if cc.has_function(f)
    cdata.set('HAVE_' + f.to_upper(), 1)
  endif
endforeach

cdata.set10('USE_MBSTATE_T', cdata.has('HAVE_WCRTOMB') or cdata.has('HAVE_MBRTOWC'))

cdata.set10('BROKEN_WCHAR_H', not cc.compiles('''
                                              #include <wchar.h>
                                              wchar_t w;
                                              ''',
                                              name: '<wchar.h> is standalone'))

if cc.has_function('nl_langinfo') and cc.has_header_symbol('langinfo.h', 'CODESET')
  cdata.set('HAVE_LANGINFO_CODESET', 1)
endif

configure_file(
  input: 'config.h.meson',
  output: 'config.h',
  configuration: cdata,
)
add_project_arguments('-DHAVE_CONFIG_H', language: 'c')

config_incdirs = include_directories('.')

subdir('include')
libiconv_public_incdirs = include_directories('include')
libiconv_internal_incdirs = [include_directories('include'), config_incdirs]

subdir('libcharset')
subdir('lib')
