# Infrastructure

Terraform is used to manage the infrastructure for the workshop's Nebula Sandbox project. It adds and provisions the necessary cloud resources for the workshop environment.

Adds `roles/owner`and necessary permissions to the project members specified in the `terraform.tfvars` file.

## Setup

To set up the infrastructure for the app, you will need to have the following tools installed:

- Install [Terraform](https://www.terraform.io/downloads) to manage the infrastructure.
    - On MacOS, you can install it using Homebrew:
        ```
        brew tap hashicorp/tap
        brew install hashicorp/tap/terraform
        ```

Create a file `terraform.tfvars` in this directory with the following content and replace the values with your project's ID and members (You can also copy it from `example.tfvars`).

```hcl
project_id      = "my-project-id"  # Replace with Nebula Sandbox project ID
project_members = ["example1@ing.com", "example2@ing.com"] # Add all project members here
```

Then run the following commands:

```bash
terraform init
terraform apply
```

Done! The terraform state is stored locally for the project, so you can't share it with others. But this should be sufficient for managing a short-lived project such as Nebula Sandbox.
