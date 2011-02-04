# mynock
# Copyright (c) 2011 Phil Christensen
#
#
# See LICENSE for details

import ez_setup
ez_setup.use_setuptools()

import os

# disables creation of .DS_Store files inside tarballs on Mac OS X
os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'

def autosetup():
	from setuptools import setup, find_packages
	return setup(
		name			= "mynock",
		version			= "1.0",
		
		packages		= find_packages('src'),
		package_dir		= {
			''			: 'src',
		},
		include_package_data = True,
		
		entry_points	= {
			'setuptools.file_finders'	: [
				'git = mynock.setup:find_files_for_git',
			]
		},
		
		install_requires = ['%s>=%s' % x for x in dict(
			django				= "1.2.4",
		).items()],
		
		# metadata for upload to PyPI
		author			= "Phil Christensen",
		author_email	= "phil@bubblehouse.org",
		description		= "an RSS Torrent feed downloader",
		license			= "MIT",
		keywords		= "mynock rss torrent bittorrent downloader",
		url				= "https://github.com/philchristensen/mynock",
	)


if(__name__ == '__main__'):
	dist = autosetup()