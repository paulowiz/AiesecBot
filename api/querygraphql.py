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

    def chamaGraphQL(self, tp_data, dt_from, dt_to, page):
        head = """{allOpportunityApplication(per_page: 500,filters:  {%s: {from:"%s", to:"%s"}},page:%s)""" % (
            tp_data, dt_from, dt_to, page)
        input_hquery = self.query_01
        input_query = head + input_hquery
        return input_query


pass
