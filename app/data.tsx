export const Users: User[] = [
    {
      id: 1,
      avatar:
        "https://images.freeimages.com/images/large-previews/971/basic-shape-avatar-1632968.jpg?fmt=webp&h=350",
      messages: [],
      name: "Legal AI",
    },
    {
      id: 2,
      avatar:
        "https://avatars.githubusercontent.com/u/114422072?s=400&u=8a176a310ca29c1578a70b1c33bdeea42bf000b4&v=4",
      messages: [],
      name: "User",
    },
  ];
  
  export const userData: User[] = [
    {
      id: 1,
      avatar:
        "https://images.freeimages.com/images/large-previews/971/basic-shape-avatar-1632968.jpg?fmt=webp&h=350",
      messages: [
        {
          id: 1,
          avatar:
            "https://avatars.githubusercontent.com/u/114422072?s=400&u=8a176a310ca29c1578a70b1c33bdeea42bf000b4&v=4",
          name: "User",
          message: "Hey!",
          timestamp: "10:01 AM",
        },
        {
          id: 2,
          avatar:
            "https://images.freeimages.com/images/large-previews/971/basic-shape-avatar-1632968.jpg?fmt=webp&h=350",
          name: "Legal AI",
          isLoading: true
        },
      ],
      name: "Legal AI",
    }
  ];
  
  export const ChatBotMessages: Message[] = [
    {
      id: 1,
      avatar: "/",
      name: "ChatBot",
      message: "Hello! How can I help you today?",
      timestamp: "10:00 AM",
      role: "ai",
    }
  ];
  
  export type UserData = (typeof userData)[number];
  
  export const loggedInUserData = {
    id: 2,
    avatar:
      "https://avatars.githubusercontent.com/u/114422072?s=400&u=8a176a310ca29c1578a70b1c33bdeea42bf000b4&v=4",
    name: "User",
  };
  
  export type LoggedInUserData = typeof loggedInUserData;
  
  export interface Message {
    id: number;
    avatar: string;
    name: string;
    message?: string;
    isLoading?: boolean;
    timestamp?: string;
    role?: string;
  }
  
  export interface User {
    id: number;
    avatar: string;
    messages: Message[];
    name: string;
  }