#   .--,       .--,
#  ( (  \.---./  ) )
#   '.__/o   o\__.'
#      {=  ^  =}
#       >  -  <
#      /       \
#     //       \\
#    //|   .   |\\
#    "'\       /'"_.-~^`'-.
#       \  _  /--'         `
#     ___)( )(___
#    (((__) (__)))    高山仰止,景行行止.虽不能至,心向往之。
from scrapy import cmdline
name = "bilichong"
cmd = "scrapy crawl {0}".format(name)
cmdline.execute(cmd.split())