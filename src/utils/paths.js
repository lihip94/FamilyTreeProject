export const backendApi = {
  serverName: "localhost:5000",
  get bashPath() {
    return `http://${this.serverName}`;
  },
};

export const backendService = {
  serviceNam: backendApi.serverName,
  getLoginPath: `${backendApi.bashPath}/login`,
  getTreeInformation: `${backendApi.bashPath}/get_tree_table`,
};
