import pytest

from bitbucket_tools.client import BitbucketClient



def test_bitbucket_client():
    client = BitbucketClient(base_url="https://api.bitbucket.org/2.0", workspace="stoneridgetechnology")
    assert client is not None
    repos = client.get_repositories()
    assert len(repos) > 0
    print(repos)

def test_bitbucket_pr_file_list():
    client = BitbucketClient(base_url="https://api.bitbucket.org/2.0", workspace="stoneridgetechnology")
    assert client is not None
    files = client.get_pr_file_list("echelon", "4300")
    assert len(files) > 0
    print(files)

