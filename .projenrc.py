from projen.python import PythonProject


AUTHORS = [
    "Jacob Petterle",
]
PROJECT = PythonProject(
    author_email="jacobpetterle@tai-tutor.team",
    author_name=AUTHORS[0],
    module_name="module_name",
    name="package-name",
    version="0.0.0",
    description="description",
    poetry=True,
    deps=[],
    dev_deps=[],
)
PROJECT.add_git_ignore("**/cdk.out")
PROJECT.add_git_ignore("**/.venv*")
PROJECT.add_task(
    "cdk-deploy-all",
    exec="cdk deploy --all --require-approval never --app 'python app.py'",
)


PROJECT.synth()
