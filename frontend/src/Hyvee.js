import { gql, useQuery } from '@apollo/client';

const LOCATIONS = {
    "Clive": [41.5774667, -93.67753619999999],
    "Cedar Falls": [42.5348993, -92.4453161],
}

//    "operationName": "SearchPharmaciesNearPointWithCovidVaccineAvailability",
//    "variables": {"radius": 50, "latitude": 41.5774667, "longitude": -93.67753619999999},
const PHARMS_WITH_VACCINE = gql`
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
`

export const HyveeVaccines = () => {
  const variables = {variables: {"radius": 50, "latitude": 41.5774667, "longitude": -93.67753619999999}}
  console.log(variables);
  console.log(PHARMS_WITH_VACCINE);
  const { loading, error, data } = useQuery(PHARMS_WITH_VACCINE, variables);

  if (loading) return 'Loading...';
  if (error) return `Error! ${error.message}`;
  console.log(data);

  return (
    <ul>
    </ul>
  )
}
