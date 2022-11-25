class vehicle_estimation_costApi(APIView):
    def post(self,request):
        data=request.data
        vehicle_type_id=data.get('vehicle_type_id')
        min_charge=data.get('min_charge')
        location_details=data.get('location_details')
        print("=>>>>",location_details)
        per_km_price=data.get('per_km_price')
        per_min_price=data.get('per_min_price')
        min_charge=data.get('min_charge')
        offer_price = data.get('offer_price')
        c = location_details['duration']
        min_value=c['text']
        # min_value =re.findall(r'\d+',min_value)
        # value2 = min_value[-2:]
        print("=dhsdjd+=====",min_value)
        int_min=min_value[0:2]
        print("===",int_min)
        int_min=int(int_min)
        int_minute=type(int_min)

        b=location_details['distance']
        km_value = b['text'] #18m
        # km_value =re.findall(r'\d+',km_value)
        print("km_value",km_value)
        # txt2=min_value.split(" ")
        # txt2=txt2[-1]
        # print(txt2)
        # print(type(txt2))
        txt=km_value[0:2]
        print("===<<<<")
        int_m=type(txt)
        print('hsdjfh',int_m)
        # txt=int(txt)
        km_txt=int(txt)
        print('shfgh',km_txt)
        # int_m=type(txt)
        # print("==,,",int_m)
        # print(txt/1000)
        # txt2=km_value[-2:]
        # print("==>>",txt2)
        # m=" m"
        # amt= VehicleTypes.objects.get(id=vehicle_type_id)
        # if txt2==m:
        #     km=txt/1000
        #     print('km',km)
        #     print("mvalue")
        #     total_amount_without_offer=int(amt.per_km_price)*(km)+int(amt.per_min_price)*int(int_min)+int(amt.min_charge)
        #     print("===<><><",total_amount_without_offer)
        #     total_amount_with_offer=int(amt.min_charge)+int(amt.per_km_price)*int(km) + int(amt.per_min_price)*int(int_min) -int( amt.offer_price)
        #     print("====<><>",total_amount_with_offer)
        #     if km==km:
        #         total_amount_without_offer=int(amt.per_min_price)*int(int_min)+int(amt.min_charge)+int(amt.per_km_price)*(km)
        #         print("===<><><",total_amount_without_offer)
        #         total_amount_with_offer=int(amt.min_charge)+int(amt.per_km_price)*(km) + int(amt.per_min_price)*int(int_min)-int( amt.offer_price)
        #         print("====<><>",total_amount_with_offer)

        return Response({
            # 'total_amount_without_offer':total_amount_without_offer,
            # 'total_amount_with_offer':total_amount_with_offer
            })





ERROR:ValueError at /api/Vehicle_estimation_cost/
invalid literal for int() with base 10: '4.'
