# k8s-preview-envs
Deployment and destruction of preview envs based on PR status 

# myapp

This repository contains the configuration and deployment setup for managing preview environments of a sample FE app using Kubernetes, Helm, and Kustomize.

- `app/`: Contains the files for the really dummy flask application
- `helm/`: Helm chart for managing Kubernetes deployment.
- `kustomize/`: Kustomize overlays for customizing dynamic preview envs.

## Helm Chart - myapp

### Chart Structure

- `Chart.yaml`: Helm chart metadata.
- `values.yaml`: Default values for Helm chart.
- `templates/`: Kubernetes manifests for Deployment and Service.


## Kustomize Overlays

Kustomize is used here to customize Helm values based on the PR name

- `kustomize/overlays/preview/kustomization.yaml`: Kustomization file for the "preview" environment. (preview dir here is an example of an adhoc environment, env name is branch name)

## Deployment Workflow

1. Build and push the Docker image of the frontend app to dorsav/myapp dockerhub registry.
2. Install the Helm chart using Kustomize for the desired environment.

   ```bash
   kubectl apply -k kustomize/overlays/preview 
Access the deployed application in the specified namespace.
Destroying Preview Environments
To destroy a preview environment, delete the corresponding Kubernetes namespace.

   ```bash
      kubectl delete -n <PR-name>
