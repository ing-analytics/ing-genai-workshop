# Infrastructure

Terraform is used to manage the infrastructure for the app.

## Setup

To set up the infrastructure for the app, you will need to have the following tools installed:

- Install [Terraform](https://www.terraform.io/downloads) to manage the infrastructure.
    - On MacOS, you can install it using Homebrew:
        ```
        brew tap hashicorp/tap
        brew install hashicorp/tap/terraform
        ```

Create a file `terraform.tfvars` in this directory with the following content and replace the values with your project's ID and members.

```hcl
project_id      = "my-project-id"
project_members = ["example1@ing.com", "example2@ing.com"] # Add all project members here
```

Then run the following commands:

```bash
terraform init
terraform apply
```

Done! The terraform state is stored locally for the project, so you can't share it with others. This should be sufficient for managing a short-lived project such as Nebula Sandbox.
