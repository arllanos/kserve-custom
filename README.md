# Custom predictor
The following example is adapted from [KServe official doc](https://kserve.github.io/website/modelserving/v1beta1/custom/custom_model/)

## Write the Custom Model Server
### Prepare dev env
```sh
virtualenv env
source env/bin/activate

pip3 install kserve
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