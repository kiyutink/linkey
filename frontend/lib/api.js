import axios from "axios";
import { camelizeKeys, decamelizeKeys } from "humps";
import { config } from "../config";

const instance = axios.create({
  baseURL: config.api.url,
  timeout: 30000
});

const camelizeInterceptor = axiosObj => {
  axiosObj.data = camelizeKeys(axiosObj.data);
  return axiosObj;
};

const decamelizeInterceptor = axiosObj => {
  axiosObj.data = decamelizeKeys(axiosObj.data);
  return axiosObj;
};

instance.interceptors.request.use(decamelizeInterceptor);
instance.interceptors.response.use(camelizeInterceptor);

export const api = {
  createLink: ({ originalUrl, hasRedirection }) =>
    instance.post("/create", {
      originalUrl,
      hasRedirection
    })
};
