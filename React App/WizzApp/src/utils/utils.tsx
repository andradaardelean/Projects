export const objectToQuery = (obj: Record<any, any>) => {
  const _query = JSON.stringify(obj);
  const query = encodeURIComponent(_query);
  return `?data=${query}`;
};

export const queryToObject = (query: string): Record<any, any> => {
  try {
    const _json = query.replace('?data=', '');
    const json = decodeURIComponent(_json);
    return JSON.parse(json);
  } catch (e) {
    return {};
  }
};
