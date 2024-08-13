from typing import Any
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

import lib
from crawlers import GithubCrawler
from db.documents import UserDocument, PostDocument  # 新增 IssueDocument
from dispatcher import CrawlerDispatcher

logger = Logger(service="github-twin/crawler")

_dispatcher = CrawlerDispatcher()
_dispatcher.register("github", GithubCrawler)

def handler(event, context: LambdaContext) -> dict[str, Any]:
    first_name, last_name = lib.user_to_names(event.get("user"))
    user = UserDocument.get_or_create(first_name=first_name, last_name=last_name)

    link = event.get("link")
    crawler = _dispatcher.get_crawler(link)

    try:
        issues = crawler.fetch_issues()  # 假設 fetch_issues 返回 issues
        for issue in issues:
            # 儲存每個 issue 到 MongoDB
            PostDocument.create(issue)  # 假設有 create 方法

        return {"statusCode": 200, "body": "Issues processed successfully"}
    except Exception as e:
        logger.error(f"Error processing issues: {str(e)}")
        return {"statusCode": 500, "body": f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    event = {
        "user": "Shirley",
        "link": "https://github.com/arealclimber", 
    }
    handler(event, None)