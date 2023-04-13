import {
    useQuery,
  } from 'react-query'

  export const useGetData = (): any => {
    return useQuery('data', async () => {
      const response = await fetch("http://api.aviationstack.com/v1/flights?access_key=8c3b220c53524bc830733c841b151762&limit=4");
      const data = await response.json();
      return data.data;
    });
  };


