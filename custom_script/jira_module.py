from jira import JIRA

KEY="wc9037hn06PP2ecVqQaSF345"
class JiraModule:
    print("sasa")
    USER = None
    USER_KEY = None
    JIRA_OBJ = None
    END_POINT = 'https://jitender1405.atlassian.net/'

    def __init__(self, user=None, api_key=None, end_point=None, /):
        self.USER = user
        self.USER_KEY = api_key
        self.END_POINT = end_point

    def basic_authentication(self):
        self.JIRA_OBJ = JIRA(self.END_POINT, basic_auth=(self.USER, self.USER_KEY))

    def get_jira_projects(self, basicAuth=True):
        if basicAuth:
            self.basic_authentication()
        return [{'id': project.id, 'name': project.name, 'key': project.key} for project in self.JIRA_OBJ.projects()]

