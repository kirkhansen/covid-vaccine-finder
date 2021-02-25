//{
//    "operationName": "SearchPharmaciesNearPointWithCovidVaccineAvailability",
//        "variables": {"radius": 50, "latitude": lat, "longitude": lon},
//        "query": (
//            "query SearchPharmaciesNearPointWithCovidVaccineAvailability("
//            "$latitude: Float!, $longitude: Float!, $radius: Int! = 40) {\n"
//            "  searchPharmaciesNearPoint(latitude: $latitude, "
//            "longitude: $longitude, "
//            "radius: $radius) {\n"
//            "    distance\n"
//            "    location {\n"
//            "      locationId\n"
//            "      name\n"
//            "      nickname\n"
//            "      phoneNumber\n"
//            "      businessCode\n"
//            "      isCovidVaccineAvailable\n"
//            "      address {\n"
//            "        line1\n"
//            "        line2\n"
//            "        city\n"
//            "        state\n"
//            "        zip\n"
//            "        latitude\n"
//            "        longitude\n"
//            "        __typename\n"
//            "      }\n"
//            "      __typename\n"
//            "    }\n"
//            "    __typename\n"
//            "  }\n"
//            "}\n"
//        ),
//}
import { request, gql } from 'graphql-request'

const query = gql`
  {
    Movie(title: "Inception") {
      releaseDate
      actors {
        name
      }
    }
  }
`
request('https://api.graph.cool/simple/v1/movies', query).then((data) => console.log(data))
