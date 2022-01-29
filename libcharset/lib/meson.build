localcharset_c = files('localcharset.c')

libcharset = library('charset', localcharset_c,
  version: libcharset_version,
  include_directories: libcharset_internal_incdirs,
  install: true,
)

libcharset_dep = declare_dependency(
  link_with: libcharset,
  include_directories: libcharset_public_incdirs,
)

pkg = import('pkgconfig')
pkg.generate(libcharset,
  name: 'libcharset',
  description: 'Portable character set determination library',
)

meson.override_dependency('libcharset', libcharset_dep)
