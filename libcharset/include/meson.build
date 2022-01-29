libcharset_h = configure_file(
  input: 'libcharset.h.in',
  output: 'libcharset.h',
  configuration: cdata,
)
localcharset_h = configure_file(
  input: 'localcharset.h.in',
  output: 'localcharset.h',
  configuration: cdata,
)
install_headers(libcharset_h, localcharset_h)
