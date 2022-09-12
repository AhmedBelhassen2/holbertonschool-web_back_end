import { createUser, uploadPhoto } from './utils';
export default function handleProfileSignup() {
    return Promise.all([uploadPhoto(), createUser()])
    .then((success) => { console.log(`${success[0].body} ${success[1].firstName} ${success[1].lastName}`); })
    .catch(() => { console.log('Signup system offline'); });
}
