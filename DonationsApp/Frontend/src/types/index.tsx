export enum UserType {
    Employee,
    User
}

export interface User {
    Id: string;
    FirstName: string;
    LastName: string;
    Email: string;
    Password: string;
    Type: UserType;
}

export interface Center {
    Id: string;
    State: string;
    City: string;
    Name: string;
    Address: string;
}

export interface Recipient {
    firstName: string;
    lastName: string;
    address: string;
}

export interface PersonalDetails {

}

export interface Donation {
    CenterId: string;
    ChildGroup: {
        Age: number;
        Sex: number;
    };
    GiftDescription: string;
    Donator: {
        FirstName: string;
        LastName: string;
        HomeAddress: string;
    }
}


export interface Task {
    id: string;
    donation: Donation;
    donationTaskStatus: number;

}