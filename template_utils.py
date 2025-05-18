from jinja2 import Environment, FileSystemLoader

# Load templates from the 'templates' directory
env = Environment(loader=FileSystemLoader('templates'))

def render_prompt(template_name, **kwargs):
    template = env.get_template(template_name)
    return template.render(**kwargs)
