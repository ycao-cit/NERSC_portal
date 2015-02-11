__author__ = 'Yi Cao <ycao@astro.caltech.edu>'


class iPTFWebsite(object):

    def __init__(self, title, contentType = "text/plain"):

        self.title = title
        self.contentType = contentType
        print "Content-Type: %s\n" % self.contentType
        self.base = "http://ptf.nersc.gov/project/deepsky/ptfvet/"


    def HTMLHeader(self):

        print "<header>"

        # style
        print '''
    <style>
        .chart {
        }

        .main text {
            font: 10px sans-serif;
        }

        .axis line, .axis path {
            shape-rendering: crispEdges;
            stroke: black;
            fill: none;
        }
    </style>
'''

        # javascript
        print '    <script type="text/javascript" src="http://d3js.org/d3.v3.min.js"></script>'

        print "</header>"


    def plaintext(self, body):

        body.print()


    def __del__(self):

        if self.contentType == "text/html":
            print "</html>"
            