genaliases = executable('genaliases', 'genaliases.c', native: true)
aliases_data = custom_target('genaliases-assets',
  output: ['aliases.gperf', 'canonical.sh', 'canonical_local.sh'],
  command: [genaliases, '@OUTPUT@', meson.current_build_dir() / 'aliases.h'],
)
aliases_h = custom_target('aliases-tmp-header',
  output: 'aliases.h',
  input: aliases_data,
  command: [gperf, '-m', '10', '@INPUT0@'],
  capture: true,
)
canonical_h = custom_target('canonical-header',
  output: 'canonical.h',
  input: [aliases_data, aliases_h],
  command: [sh, '@INPUT1@'],
  capture: true,
)
canonical_local_h = custom_target('canonical-local-header',
  output: 'canonical_local.h',
  input: [aliases_data, aliases_h],
  command: [sh, '@INPUT2@'],
  capture: true,
)

genflags = executable('genflags', 'genflags.c', native: true)
flags_h = custom_target('flags.h',
  output: 'flags.h',
  command: [genflags],
  capture: true,
)

gentranslit = executable('gentranslit', 'gentranslit.c', native: true)
translit_h = custom_target('translit.h',
  output: 'translit.h',
  input: 'translit.def',
  command: [gentranslit],
  feed: true,
  capture: true,
)

sources = [
  'iconv.c',
  localcharset_c,
  aliases_h,
  canonical_h,
  canonical_local_h,
  flags_h,
  translit_h,
]

libiconv = library('iconv', sources,
  version: libiconv_version,
  include_directories: [libiconv_internal_incdirs, libcharset_internal_incdirs],
  install: true,
)

libiconv_dep = declare_dependency(
  link_with: libiconv,
  include_directories: libiconv_public_incdirs,
)

pkg = import('pkgconfig')
pkg.generate(libiconv,
  name: 'libiconv',
  description: 'Character set conversion library',
)

meson.override_dependency('libiconv', libiconv_dep)
