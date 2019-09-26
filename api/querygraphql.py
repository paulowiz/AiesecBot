class queryGraphql:

    def __init__(self):

        self.query_01 = """
    {
    paging {
      total_pages
      current_page
      total_items
    }
    data {
      id
      status
      created_at
      date_matched
      date_approved
      date_realized
      experience_start_date
      experience_end_date
      date_approval_broken
      nps_response_completed_at
      updated_at
      person {
        id
        home_mc {
          id
          name
        }
        home_lc {
          id
          name
        }
      }
      host_lc {
        id
        name
      }
      home_mc {
        id
        name
      }
      opportunity {
        id
				created_at
        title
        available_openings
        duration
        
        sub_product{
          name
        }
        programme {
          id
          short_name_display
        }
      }
      standards {
        option
      }
    }
  }
}
              """

    def chamaGraphQL(self, page):
        head = """{allOpportunityApplication(per_page: 200,filters:  {date_approved: {from:"2016-01-01T00:00:01Z", to:"2017-04-31T23:59:59Z"},person_home_mc:1606},page:%s)""" % (page)
        input_hquery = self.query_01
        input_query = head + input_hquery
        return input_query


pass
