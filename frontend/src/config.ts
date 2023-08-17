const config: { apiUrl: string } = {
    apiUrl: import.meta.env.AWS_API_GATEWAY_URL || ""
}

export default config