# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# extract_cchat_log: Extract a comic chat log from its OLE2 container and write
# it to stdout
#
# While Comic Chat is an OLE2 compliant app that can embed logs into other OLE2
# applications, it does so using OLE Structured Storage. This is a bit of a
# pain, because it doesn't use the format for anything else. Thankfully, this
# makes extraction a simple operation: take out the contents stream, and it's
# plain text that can be parsed manually. That's an issue for another day after
# sucking the log out of its container.

import sys
import olefile

def main():
	# kill the invoker name
	sys.argv.pop(0);
	for f in sys.argv:
		ole = olefile.OleFileIO(f)
		log = ole.openstream("Contents")
		log_text = log.read()
		print log_text

main()
