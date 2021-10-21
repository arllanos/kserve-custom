# Custom predictor
The following example is adapted from [KServe official doc](https://kserve.github.io/website/modelserving/v1beta1/custom/custom_model/)

## Pre-requisites
[Install KServe 0.7.0] https://kserve.github.io/website/admin/serverless/

> ℹ️ **Or run the one liner installer from kubeflow-manifests as long as it as been already upgraded to v0.7.0**

## Write the Custom Model Server
### Prepare dev env
```sh
virtualenv env
source env/bin/activate

pip3 install kserve
pip install 'ray[default]'
pip3 freeze > requirements.txt
```
> ℹ️ **there is no need to install ray package separately**

### Build with buildpack and push
```sh
export DOCKER_USER=arllanos

pack build --builder=heroku/buildpacks:20 ${DOCKER_USER}/custom-model:v2
docker push ${DOCKER_USER}/custom-model:v2

```
## Deploy inference
```sh
kubectl apply -f custom.yaml
```