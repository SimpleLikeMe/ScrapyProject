from scrapy import cmdline
name = 'yiwugou'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
