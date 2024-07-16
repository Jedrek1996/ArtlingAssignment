## Steps for assignment - Jedrek

After setting up the docker env, and ran both images to ensure connectivity.
I tackled the backend portion first.

## Backend ✨

The task was to create a date in the function get_member_since_str.

1. Checked if the date_joined is set, if not it will return a "Date Joined" string.
2. Retrieved the current date time via the datetime lib.
3. Calculated the difference of date (current date in Step2. & date joined) via the relativedelta lib.
4. Return the value in Step3. based on the assignment string structure.

## Test Cases ✨

test_get_member_since_str

1. Similarly, the test case replicates the expected results from the function. By mocking the object
2. Added a join date of 365 days ago to simulate.
3. Calculate the difference and return the string. Exactly from the function.

test_team_list_view_get

1. This test case mocks the response data from the teams endpoint.
2. To ensure that the data are returned correctly, and there is no issue connecting to the endpoint.

## Frontend ✨

1. For the frontend, it is essential to ensure that it is able to retrieve the data from localhost:8000. Once this is established, the usersData are mapped and each individual userData is rendered.
2. Once done, styling is applied via tailwind.css and the custom styles that are in tailwind.config.ts.
3. The responsize design is communicated via sm, md etc. Thus in order to recreate the responsive layout, md was used.
4. Grid and flex box were used to style the component. Grid was used to display the no. of users while within the user component flexbox was used for a 1d layout.
5. Also recommend the creation of a proxy instead of hardcoding the localhost URL.
