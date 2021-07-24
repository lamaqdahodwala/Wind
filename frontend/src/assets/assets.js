import { getCookie } from "./helpers.js";

export async function send_gql_request(data){
    let resp = await fetch('/graphql', {
        method: "POST",
        headers: {
            "X-CSRFToken": getCookie('csrftoken')
        },
        cache: 'no-cache',
        body: JSON.parse(data)
    })
    let txt = await resp.json()
    return txt;
}