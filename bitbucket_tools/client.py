from typing import List, Optional, Dict, Any
from bitbucket_tools.pr_parser import parse_pr_file_list
import base64
import os
import requests
from requests.auth import HTTPBasicAuth

# from llama_index.readers.base import BaseReader
# from llama_index.readers.schema.base import Document


class BitbucketClient   :
    """Bitbucket reader.

    Reads the content of files in Bitbucket repositories.

    """

    def __init__(
        self,
        base_url: str,
        workspace: str,
        repository: Optional[str] = None,
        extensions_to_skip: Optional[List] = []
    ) -> None:
        if os.getenv("BITBUCKET_USERNAME") is None:
            raise ValueError("Could not find a Bitbucket username.")
        if os.getenv("BITBUCKET_APP_PASSWORD") is None:
            raise ValueError("Could not find a Bitbucket app key.")
        if base_url is None:
            raise ValueError("You must provide a base url for Bitbucket.")
        self.base_url = base_url
        self.workspace = workspace
        self.repository = repository
        self.extensions_to_skip = extensions_to_skip

    def get_repositories(self) -> List[str]:
        url = f"{self.base_url}/repositories/{self.workspace}"
        response = requests.get(url, auth=HTTPBasicAuth(os.getenv("BITBUCKET_USERNAME"), os.getenv("BITBUCKET_APP_PASSWORD")))
        if response.status_code != 200:
            raise Exception(f"Failed to get repositories: {response.status_code} {response.text}")
        data = response.json()
        repos = []
        for repo in data.get('values', []):
            repos.append(repo['name'])
        return repos
        

    def get_pr_file_list(self, repo, pr_id: str) -> List[str]:
        url = f"{self.base_url}/repositories/{self.workspace}/{repo}/pullrequests/{pr_id}/diffstat"
        response = requests.get(url, auth=HTTPBasicAuth(os.getenv("BITBUCKET_USERNAME"), os.getenv("BITBUCKET_APP_PASSWORD")))
        if response.status_code != 200:
            raise Exception(f"Failed to get pull request: {response.status_code} {response.text}")
        data = response.json()
        files = parse_pr_file_list(data)
        
        # print(data['links']['diff'])
        
        return files
    