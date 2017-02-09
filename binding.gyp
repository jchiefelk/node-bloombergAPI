{
  'targets': [

    {
      'target_name': 'bloomberg',
      'sources': [ './build/addons/bloomberg.cpp' ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'conditions': [
          ['OS=="mac"', {
          'include_dirs': [
            '<(module_root_dir)/deps/blpapi/include-3.8.1.1'
          ],
          'ldflags': [
            '-Wl,-rpath,<(module_root_dir)/deps/blpapi/osx',
            '-L<(module_root_dir)/deps/blpapi/osx'
          ],
          'conditions': [
            ['target_arch=="ia32"', {
              'libraries': [ '-lblpapi3_32' ],
              'xcode_settings': { 'ARCHS': [ 'i386' ] }
            }],
            ['target_arch=="x64"', {
              'libraries': [ '-lblpapi3_64' ],
              'xcode_settings': { 'ARCHS': [ 'x86_64' ] }
            }]
          ],
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'GCC_ENABLE_CPP_RTTI': 'NO',
            'INSTALL_PATH': '@rpath',
            'LD_DYLIB_INSTALL_NAME': '',
            'OTHER_LDFLAGS': [
              '-Wl,-search_paths_first',
              '-Wl,-rpath,<(module_root_dir)/deps/blpapi/osx',
              '-L<(module_root_dir)/deps/blpapi/osx'
            ]
          }
        }],
          ['OS=="linux"', {
          'include_dirs': [
            '<(module_root_dir)/deps/blpapi/include-3.8.8.1'
          ],
          'ldflags': [
            '-Wl,-R<(module_root_dir)/deps/blpapi/linux',
            '-L<(module_root_dir)/deps/blpapi/linux'
          ],
          'conditions': [
            ['target_arch=="ia32"', {
              'libraries': [ '-lblpapi3_32' ]
            }],
            ['target_arch=="x64"', {
              'libraries': [ '-lblpapi3_64' ]
            }]
          ]
        }]

      ]
    },

    {
        "target_name": "returnobject",
        "sources":  ["./build/addons/returnobject.cc"] 
    }
  ]

}