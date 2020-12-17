class MarketRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label== 'Market' :
            return 'Market'
        return None


    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Market' :
            return 'Market'
        return None

    #def allow_migrate(self,)
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'Market' :
            return db == 'Market' 