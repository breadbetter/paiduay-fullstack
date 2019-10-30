import axios from 'axios'

const mainAxios = axios.create({
    baseURL: 'http://localhost:8000/api/v1/'
})

export default mainAxios