/** @format */

import axios from 'axios';
import Cookies from 'js-cookie';
import { useMutation, useQuery, useQueryClient } from 'react-query';
import { Center, User } from '~/types';

const authURL = 'http://localhost:12500/auth';

const locationURL = 'http://localhost:12600/location';

const donationURL = 'http://localhost:12700/donation';

const taskURL = 'http://localhost:12800/task';

axios.defaults.withCredentials = true;

// ------------------ Auth ------------------

export const useCreateUser = () => {
	return useMutation((user: User) => {
		return axios.post(
			`${authURL}/createAccount`,
			{
				FirstName: user.FirstName,
				LastName: user.LastName,
				Email: user.Email,
				Password: user.Password,
			},
			{
				headers: {
					'Access-Control-Allow-Origin': '*',
					'Content-Type': 'application/json',
				},
			},
		);
	});
};

export const useLogIn = () => {
	return useMutation((authUser: any) => {
		return axios.post(
			`${authURL}/login`,
			{ Email: authUser.Email, Password: authUser.Password },
			{
				headers: {
					'Access-Control-Allow-Origin': '*',
					'Content-Type': 'application/json',
				},
			},
		);
	});
};

export const useLogOut = () => {
	return useMutation((authUser: any) => {
		return authUser;
	});
};


// ------------------ Location ------------------

export const useGetStates = () => {
	return useQuery('locationByState', () => {
		return axios.post(`${locationURL}/getStates`);
	});
};

export const useGetCitiesByState = (state: string) => {
	return useQuery('citiesByState', () => {
		return axios.post(`${locationURL}/getCities`, {
			State: state,
		});
	});
};

export const useGetCenters = (city: string, state: string) => {
	return useQuery('centersByCity', () => {
		return axios.post(`${locationURL}/getCenters`, {
			City: city,
			State: state,
		});
	});
};

// ------------------ Center ------------------

export const useCreateCenter = () => {
	return useMutation((center: Center) => {
		return axios.post(`${locationURL}/addCenter`, {
			State: center.State,
			City: center.City,
			Name: center.Name,
			Address: center.Address,
		});
	});
};

// ------------------ Donor ------------------

export const useAddDonation = () => {
	return useMutation((data: any) => {
		return axios.post(`${donationURL}/addDonation`, {
			CenterId: data.CenterId,
			ChildGroup: data.ChildGroup,
			GiftDescription: data.GiftDescription,
			Donator: data.Donator,
		});
	});
};


// ------------------ Task ------------------

export const useGetTasks = () => {
	return useQuery('tasks', () => {
		return axios.post(`${taskURL}/get/all`);
	});
}

export const useGetMyInProgressTasks = () => {
	return useQuery('myprogresstasks', () => {
		return axios.post(`${taskURL}/get`, {
			EmployeeId: Cookies.get('userId') ?? '',
			donationTaskStatus: 1,
		});
	});
}

export const useGetMyCompletedTasks = () => {
	return useQuery('mycompletedtasks', () => {
		return axios.post(`${taskURL}/get`, {
			EmployeeId: Cookies.get('userId') ?? '',
			donationTaskStatus: 2,
		});
	});
}

export const useCreateTask = () => {
	return useMutation((task: any) => {
		return axios.post(`${taskURL}/createTask`, {
			Task: task,
		});
	});
}

export const useCompleteTask = () => {
	const queryClient = useQueryClient();
	return useMutation((taskId: any) => {
		return axios.post(`${taskURL}/update`, {
			TaskId: taskId,
			EmployeeId: Cookies.get('userId') ?? '',
			DonationTaskStatus: 2,
		}).then(() => {
			queryClient.invalidateQueries(['myprogresstasks', 'mycompletedtasks']); // Invalidate multiple queries
		});;
	});
}

export const useAssignTask = () => {
	const queryClient = useQueryClient();
	return useMutation((taskId: any) => {
		return axios.post(`${taskURL}/update`, {
			TaskId: taskId,
			EmployeeId: Cookies.get('userId') ?? '',
			DonationTaskStatus: 1,
		}).then(() => {
			queryClient.invalidateQueries(['tasks', 'myprogresstasks', 'mycompletedtasks']); // Invalidate multiple queries
		});;
	});
}