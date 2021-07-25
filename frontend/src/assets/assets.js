import { getCookie } from "./helpers.js";

export async function send_gql_request(data){
    
    let resp = await fetch('/graphql', {
        method: "POST",
        body: JSON.stringify({
            "query": data,
            variables: null
        }),
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
            "Content-Type": "application/json"
        }
    })
    return await resp.json()
}