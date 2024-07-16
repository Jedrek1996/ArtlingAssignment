import { LoaderFunction } from "@remix-run/node";
import { useLoaderData } from "@remix-run/react";
import axios from "axios";

export default function TeamView() {
  const usersData = useLoaderData<any>();

  return (
    <main className="md:mx-auto md:container mx-5">
      <h1 className="text-h1 font-semibold font-seriff mb-2">The Team</h1>
      <p className="text-p1 mb-4 font-medium ">
        We at the Artling are passionate about Art and we aim to provide the
        best service possible to our clients. We're always looking out for
        talented people.
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {usersData.map((userData: any) => {
          // console.log(userData);
          return (
            <div key={userData.id} className="flex items-start overflow-hidden border-b-2 border-gray-border pb-6 md:border-b-0">
              <img
                src={`http://localhost:8000/media/${userData.image}`}
                alt={userData.name}
                className="object-cover w-20 h-20 mt-2 rounded-full"
              />
              <div className="flex-1 px-4">
                <h4 className="text-h4 text-brand-gold font-semibold">
                  {userData.name}
                </h4>
                <p className="text-p1 text-text-muted font-normal">
                  {userData.member_since_str}
                </p>
                <p className="text-p1 font-medium">{userData.bio}</p>
              </div>
            </div>
          );
        })}
      </div>
    </main>
  );
}

export let loader: LoaderFunction = async ({ request, params }) => {
  const response: any = await axios({
    url: "http://django-backend:8000/team/",
    method: "GET",
  }).catch((err: any) => {
    console.log("AXIOS ERROR: ", { err });
  });

  return response.data.data;
};
