"""Module to handle model loading and using it to predict urls"""
import joblib
from metrics_calculators import calculate_metrics, transform
from typing import Optional


class Model():
    """
    Examples
    --------
    >>> model = Model()
    >>> print(model.predict("https://a11egro.pl"))
    'bad'
    """
    def __init__(self, model_file: Optional[str] = "Dumps/model.sav",
                 scaler_file: Optional[str] = "Dumps/scaler.sav",
                 encoder_file: Optional[str] = "Dumps/encoder.sav"):
        """
        Creates model from given files.

        Parameters
        ----------
        model_file: str
            Name of file to witch model was dumped. Default: "Dumps/model.sav"
        scaler_file : str
            Name of file to witch StandardScaler was dumped. Default: "Dumps/scaler.sav"
        encoder_file : str
            Name of file to witch LabelEncoder was dumped. Default: "Dumps/encoder.sav"
        """
        self.model = joblib.load(model_file)
        self.scaler = joblib.load(scaler_file)
        self.encoder = joblib.load(encoder_file)


    def predict(self, url: str) -> str:
        """
        Predicts whether url is bad or good.

        Parameters
        ----------
        url : str
            Url to predict.

        Returns
        -------
        str
            Either 'good' or 'bad'.

        """
        return self.encoder.inverse_transform(self.model.predict(self.scaler.transform(calculate_metrics(transform(url)))))[0]


