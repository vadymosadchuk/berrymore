from dateutil import parser

from .models import Visit


class ReportDaily:
    def __init__(self, date):
        super().__init__()
        self.date_start_raw, self.date_end_raw = date.split('_')
        self.date_start, self.date_end = parser.parse(self.date_start_raw), parser.parse(self.date_end_raw)

    def get_visits(self):
        return Visit.objects.filter(datetime__date__gte=self.date_start,
                                    datetime__date__lte=self.date_end).order_by('created')

    def get_report(self):
        visits = list(self.get_visits())
        products = {}
        for visit in visits:
            if visit.product in products:
                products[visit.product]['visits'].append(visit)
            else:
                products[visit.product] = {
                    'visits': [visit]
                }

        for product, data in products.items():
            products[product]['total_weight'] = sum([x.weight for x in data['visits']])
            products[product]['total_number_of_boxes'] = sum([x.number_of_boxes for x in data['visits']])
            products[product]['total_number_of_boxes_in'] = sum([x.number_of_boxes_in for x in data['visits']])
            products[product]['total_number_of_boxes_out'] = sum([x.number_of_boxes_out for x in data['visits']])
            products[product]['total_netto'] = round(sum([x.get_netto() for x in data['visits']]))
            products[product]['total_price'] = round(sum([x.get_price() for x in data['visits']]), 2)

        return {
            'products': products,
            'date_start': self.date_start_raw,
            'date_end': self.date_end_raw,
        }
