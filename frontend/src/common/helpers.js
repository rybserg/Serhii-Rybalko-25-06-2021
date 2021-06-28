export default {
  objectToQueryString(params) {
    if (typeof params === "object" && params !== null) {
      return Object.keys(params)
        .map((key) => key + "=" + params[key])
        .join("&");
    }
    return "";
  },
};
