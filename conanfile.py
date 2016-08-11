from conans import ConanFile
from conans.tools import get


class MapboxVariantConan(ConanFile):
    name = 'mapbox-variant'
    version = '1.1.2'
    author = 'Hinrik Gylfason (hinrikg@gmail.com)'
    url = 'http://github.com/hinrikg/conan-mapbox-variant'
    license = 'MIT'

    settings = None
    generators = 'cmake'

    def source(self):
        get('https://github.com/mapbox/variant/archive/v1.1.2.zip')

    def package(self):
        self.copy('*.hpp', dst='include', src='variant-1.1.2/include', keep_path=True)
        self.copy('LICENSE', dst='.', src='variant-1.1.2')
        self.copy('LICENSE_1_0.txt', dst='.', src='variant-1.1.2')
