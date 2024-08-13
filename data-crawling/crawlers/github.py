import os
import requests
from dotenv import load_dotenv
from aws_lambda_powertools import Logger

logger = Logger(service="github-twin/issue-crawler")

class GithubCrawler:
    BASE_URL = "https://api.github.com"
    
    def __init__(self) -> None:
        load_dotenv();
        self.org = os.getenv("GITHUB_ORG")
        self.user = os.getenv("GITHUB_USER")
        self.token = os.getenv("GITHUB_TOKEN")
        # self.org = org
        # self.user = user
        # self.token = token
        # print("GITHUB_ORG", self.org)


    def fetch_issues(self):
        url = f"{self.BASE_URL}/orgs/{self.org}/issues"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
        }
        params = {
            "per_page": 100,
            "page": 1
        }
        
        logger.info(f"Fetching issues for organization: {self.org} assigned to user: {self.user}")
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            issues = response.json()
            for issue in issues:
                if issue.get("assignee") and issue["assignee"]["login"] == self.user:
                    label_names = [label["name"] for label in issue["labels"]]
                    logger.info(f"Issue found: {issue['title']} - {issue['html_url']} ({issue['state']}) ({label_names})")  # 加入state標註                        
        else:
            logger.error(f"Failed to fetch issues: {response.status_code} - {response.text}")


if __name__ == "__main__":
    crawler = GithubCrawler()
    crawler.fetch_issues()
