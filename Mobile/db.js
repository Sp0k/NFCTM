import { createApi, fakeBaseQuery } from "@reduxjs/toolkit/query/react";
import uuid from "react-native-uuid";
import AsyncStorage from "@react-native-async-storage/async-storage";

export const dbApi = createApi({
  reducerPath: "dbApi",
  tagTypes: ["Tasks"],
  baseQuery: fakeBaseQuery(),
  endpoints: (build) => ({
    fetchTasks: build.query({
      async queryFn() {
        const serializedTasks = await AsyncStorage.getItem("tasks");
        const tasks = JSON.parse(serializedTasks);

        return { data: [tasks] };
      },
      providesTags: (results) => ["Tasks"],
    }),
    searchTasks: build.query({
      async queryFn(searchString) {
        const serializedTasks = await AsyncStorage.getItem("tasks");

        const tasks = JSON.parse(serializedTasks);

        if (searchString == "") {
          return { data: tasks || [] };
        } else {
          const filteredTasks = tasks.filter((task) => {
            const { title, due_date, priority, description } = note;
            const s = searchString.toLocaleLowerCase();
            return (
              title.toLowerCase().indexOf(s) !== -1 ||
              Content.toLowerCase().indexOf(s) !== -1
            );
          });

          return { data: filteredTasks || [] };
        }
      },
      providesTags: (result) => ["Tasks"],
    }),
    addTask: build.mutation({
      async queryFn(task) {
        const serializedTasks = await AsyncStorage.getItem("tasks");
        const tasks = JSON.parse(serializedTasks) || [];
        task.id = uuid.v4();
        tasks.unshift(task);
        await AsyncStorage.setItem("tasks", JSON.stringify(tasks));
        return { data: task };
      },
      invalidatesTags: ["Tasks"],
    }),
    deleteTask: build.mutation({
      async queryFn(task) {
        const serializedTasks = await AsyncStorage.getItem("tasks");
        let tasks = JSON.parse(serializedTasks) || [];
        tasks = tasks.filter((x) => x.id !== task.id);
        await AsyncStorage.setItem("tasks", JSON.stringify(tasks));
        return { data: note };
      },
    }),
    updateTask: build.mutation({
      async queryFn(task) {
        const serializedTasks = await AsyncStorage.getItem("tasks");
        const tasks = JSON.parse(serializedTasks) || [];
        const updatedTasks = tasks.map((t) => {
          if (t.id === task.id) {
            return {
              ...t,
              title: task.title,
              due_date: task.due_date,
              priority: task.priority,
              description: task.description,
            };
          }
          return t;
        });
        await AsyncStorage.setItem("tasks", JSON.stringify(updatedTasks));
        return { data: task };
      },
      invalidatesTags: ["Tasks"],
    }),
  }),
});

export const {
  useFetchTasksQuery,
  useSearchTasksQuery,
  useAddTaskMutation,
  useUpdateTaskMutation,
  useDeleteTaskMutation,
} = dbApi;
