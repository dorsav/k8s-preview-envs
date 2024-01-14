# k8s-preview-envs
Deployment and destruction of preview envs based on PR status 

# myapp

This repository contains the configuration and deployment setup for managing preview environments of a sample FE app using Kubernetes, Helm, and Kustomize.

- `app/`: Contains the files for the FE application (Mainly Dockerfile).
- `helm/`: Helm chart for managing Kubernetes deployment.
- `kustomize/`: Kustomize overlays for customizing Helm charts based on environments.

## Helm Chart - myapp

### Chart Structure

- `Chart.yaml`: Helm chart metadata.
- `values.yaml`: Default values for Helm chart.
- `templates/`: Kubernetes manifests for Deployment and Service.


### Customize Helm Values

Update `helm/myapp/values.yaml` to customize deployment settings such as replica count, image repository, and service type.

## Kustomize Overlays

Kustomize is used here to customize Helm values based on the PR name

- `kustomize/overlays/preview/kustomization.yaml`: Kustomization file for the "preview" environment.

## Deployment Workflow

1. Build and push the Docker image for the frontend app to your container registry.
2. Install the Helm chart using Kustomize for the desired environment.

   ```bash
   kubectl apply -k kustomize/overlays/preview
Access the deployed application in the specified namespace.
Destroying Preview Environments
To destroy a preview environment, delete the corresponding Kubernetes namespace.

   ```bash
      helm uninstall my-frontend-app -n <PR-name>
