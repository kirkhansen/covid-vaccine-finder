import { request, gql } from "graphql-request"

const LOCATIONS = {
    "Clive": [41.5774667, -93.67753619999999],
    "Cedar Falls": [42.5348993, -92.4453161],
}

//    "operationName": "SearchPharmaciesNearPointWithCovidVaccineAvailability",
//    "variables": {"radius": 50, "latitude": 41.5774667, "longitude": -93.67753619999999},
const uri = "https://www.hy-vee.com/my-pharmacy/api/graphql"
const query = gql`
{
    query SearchPharmaciesNearPointWithCovidVaccineAvailability(
    $latitude: Float!, $longitude: Float!, $radius: Int! = 40) {
      searchPharmaciesNearPoint(latitude: $latitude,
    longitude: $longitude,
    radius: $radius) {
        distance
        location {
          locationId
          name
          nickname
          phoneNumber
          businessCode
          isCovidVaccineAvailable
          address {
            line1
            line2
            city
            state
            zip
            latitude
            longitude
            __typename
          }
          __typename
        }
        __typename
      }
    }
}
`
request(uri, query, {"radius": 50, "latitude": 41.5774667, "longitude": -93.67753619999999}).then((data) => console.log(data))
