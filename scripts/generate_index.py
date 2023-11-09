import json
import hashlib
import os

from pkginfo import Wheel

PYPI_PREFIX = 'https://test-files.pythonhosted.org/packages'

def read_chunks(h, filename):
    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)


def sha256sum(filename):
    h = hashlib.sha256()
    read_chunks(h, filename)
    return h.hexdigest()


def blake2b256(filename):
    h = hashlib.blake2b(digest_size=32)
    read_chunks(h, filename)
    return h.hexdigest()


def package_version_entry(download_url, filename, meta, sha256):
    return {
        'downloadUrl': download_url,
        'filename': filename,
        'metadata': {
            'classifiers': meta.classifiers,
            'extensions': {
                'python.details': {
                    'contacts': [
                        {
                            'email': meta.author_email,
                            'name': meta.author,
                            'role': 'author'
                        }
                    ],
                    'project_urls': {
                        'Home': meta.home_page
                    }
                }
            },
            'license': meta.license,
            'metadata_version': meta.metadata_version,
            'name': meta.name,
            'summary': meta.summary,
            'version': meta.version
        },
        'sha256Digest': sha256
    }


def main():
    packages = {}

    dist = 'dist'
    for pkg_name in os.listdir(dist):
        full_path = os.path.join(dist, pkg_name)
        meta = Wheel(full_path)
        sha256 = sha256sum(full_path)
        blake2b = blake2b256(full_path)
        if meta.name not in packages:
            packages[meta.name] = []
        download_url = f'{PYPI_PREFIX}/{blake2b[0:2]}/{blake2b[2:4]}/{blake2b[4:]}/{pkg_name}'
        version_entry = package_version_entry(download_url, pkg_name, meta, sha256)

        packages[meta.name].append(version_entry)

    res = {
        'extensions': packages
    }

    with open('index.json', 'w') as f:
        json.dump(res, f, indent=True)


if __name__ == '__main__':
    main()
