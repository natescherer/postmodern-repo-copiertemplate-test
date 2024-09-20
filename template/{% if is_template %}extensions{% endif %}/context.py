from copier_templates_extensions import ContextHook


class ContextUpdater(ContextHook):
    update = False

    def hook(self, context):
        # Doing the below ensures that repo actions are only taken on the
        # first, interactive run of the template, not on subsequent updates
        if "repo_actions" in context["_copier_answers"]:
            del context["_copier_answers"]["repo_actions"]