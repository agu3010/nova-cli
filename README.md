## NOVA command line access

### Installation

Install the script with

    $ python setup.py install


### Usage

The `nova` tool is similar to the `git` revision control system binary. Use
`nova config` to configure local and global configuration options. For example
to set the remote server and access token use

    $ nova config core.token 23.asx0993m348a
    $ nova config core.remote https://somewhere.over.the.rainbow

If you do not save them globally you always pass them as command line arguments
`--remote` and `--token` respectively. They will be saved for the dataset if
necessary. To get a list of all commands type

    $ nova --help
