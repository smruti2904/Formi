from jinja2 import Template

# Open and read the template file
with open("prompts/booking_prompt.jinja") as f:
    template = Template(f.read())

# Render the template with variables
output = template.render(
    customer_name="Aryamann",
    booking_date="2025-06-01",
    outlet_name="Indiranagar",
    num_guests=4
)

print(output)
