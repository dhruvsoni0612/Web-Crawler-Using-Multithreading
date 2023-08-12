from multi_threaded_crawler import MultiThreadedCrawler

if __name__ == '__main__':
    cc = MultiThreadedCrawler("https://stackoverflow.com/")
    cc.run_web_crawler()
    cc.info()