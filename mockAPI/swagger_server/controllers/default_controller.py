import connexion
import json 
import six

from swagger_server.models.image_url import ImageUrl  # noqa: E501
from swagger_server import util


def a165c19b6a1574d4c8971af47():  # noqa: E501
    """Get Batch List (Internal)

     # noqa: E501


    :rtype: None
    """
    return ''


def a56f91f2e778daf14a499f200(language=None, model_version=None, body=None):  # noqa: E501
    """Tag Image

    This operation generates a list of words, or tags, that are relevant to the content of the supplied image. The Computer Vision API can return tags based on objects, living beings, scenery or actions found in images. Unlike categories, tags are not organized according to a hierarchical classification system, but correspond to image content. Tags may contain hints to avoid ambiguity or provide context, for example the tag \&quot;ascomycete\&quot; may be accompanied by the hint \&quot;fungus\&quot;.          &lt;br&gt;          &lt;br&gt;          Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.            &lt;br&gt;          &lt;br&gt;          A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.     &lt;h4&gt;Http Method&lt;/h4&gt;  POST # noqa: E501

    :param language: A string indicating the language in which to return tags. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;. See https://aka.ms/cv-languages for list of supported languages.
    :type language: str
    :param model_version: Optional parameter to specify the version of the AI model. The default value is \&quot;latest\&quot;.
    :type model_version: str
    :param body: Input passed within the POST body. Supported input methods: raw image binary or image URL.   &lt;br/&gt;  &lt;br/&gt;Input requirements:   &lt;ul&gt;  &lt;li&gt;Supported image formats: JPEG, PNG, GIF, BMP. &lt;/li&gt;  &lt;li&gt;Image file size must be less than 4MB.&lt;/li&gt;  &lt;li&gt;Image dimensions should be greater than 50 x 50.&lt;/li&gt;  &lt;/ul&gt;
    :type body: 

    :rtype: None
    """
    temp_tag = '''{"tags":[{"name":"grass","confidence":0.9999997615814209},{"name":"outdoor","confidence":0.99997067451477051},{"name":"sky","confidence":0.99928975105285645},{"name":"building","confidence":0.99646323919296265},{"name":"house","confidence":0.99279803037643433},{"name":"lawn","confidence":0.82268029451370239},{"name":"green","confidence":0.64122253656387329},{"name":"residential","confidence":0.31403225660324097}],"requestId":"1ad0e45e-b7b4-4be3-8042-53be96103337","metadata":{"width":400,"height":400,"format":"Jpeg"},"modelVersion":"2021-04-01"}'''
    return json.loads(temp_tag)


def a56f91f2e778daf14a499f20c(width, height, smartCropping=None, model_version=None, body=None):  # noqa: E501
    """Get Thumbnail

    This operation generates a thumbnail image with the user-specified width and height.  By default, the service analyzes the image, identifies the region of interest (ROI), and generates smart cropping coordinates based on the ROI.  Smart cropping helps when you specify an aspect ratio that differs from that of the input image  &lt;p/&gt;  A successful response contains the thumbnail image binary.  If the request failed, the response contains an error code and a message to help determine what went wrong.    &lt;p/&gt;  Upon failure, the error code and an error message are returned. The error code could be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, InvalidThumbnailSize, NotSupportedImage, FailedToProcess, Timeout, or InternalServerError.    &lt;h4&gt;Http Method&lt;/h4&gt;  POST   # noqa: E501

    :param width: Width of the thumbnail.  It must be between 1 and 1024. Recommended minimum of 50.
    :type width: 
    :param height: Height of the thumbnail. It must be between 1 and 1024. Recommended minimum of 50.
    :type height: 
    :param smartCropping: Boolean flag for enabling smart cropping.
    :type smartCropping: bool
    :param model_version: Optional parameter to specify the version of the AI model. The default value is \&quot;latest\&quot;.
    :type model_version: str
    :param body: Input passed within the POST body. Supported input methods: raw image binary or image URL.   &lt;br/&gt;  &lt;br/&gt;Input requirements:   &lt;ul&gt;  &lt;li&gt;Supported image formats: JPEG, PNG, GIF, BMP. &lt;/li&gt;  &lt;li&gt;Image file size must be less than 4MB.&lt;/li&gt;  &lt;li&gt;Image dimensions should be greater than 50 x 50.&lt;/li&gt;  &lt;/ul&gt;
    :type body: 

    :rtype: None
    """
    return 'do some magic!'


def a56f91f2e778daf14a499f20d(language=None, detectOrientation=None, model_version=None, body=None):  # noqa: E501
    """OCR

    Optical Character Recognition (OCR) detects text in an image and extracts the recognized characters into a machine-usable character stream.       &lt;p/&gt;  Upon success, the OCR results will be returned.   &lt;p/&gt;  Upon failure, the error code together with an error message will be returned. The error code can be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, NotSupportedImage,  NotSupportedLanguage, or InternalServerError.    &lt;h4&gt;Http Method&lt;/h4&gt;  POST # noqa: E501

    :param language: The BCP-47 language code of the text to be detected in the image.The default value is &amp;quot;unk&amp;quot;, then the service will auto detect the language of the text in the image.&lt;br /&gt;     &lt;br /&gt;     Supported languages:     &lt;ul style&#x3D;\&quot;margin-left:.375in;direction:ltr;unicode-bidi:embed;  margin-top:0in;margin-bottom:0in\&quot; type&#x3D;\&quot;disc\&quot;&gt;         &lt;li&gt;unk (AutoDetect)&lt;/li&gt;         &lt;li&gt;zh-Hans (ChineseSimplified)&lt;/li&gt;         &lt;li&gt;zh-Hant (ChineseTraditional)&lt;/li&gt;         &lt;li&gt;cs (Czech)&lt;/li&gt;         &lt;li&gt;da (Danish)&lt;/li&gt;         &lt;li&gt;nl (Dutch)&lt;/li&gt;         &lt;li&gt;en (English)&lt;/li&gt;         &lt;li&gt;fi (Finnish)&lt;/li&gt;         &lt;li&gt;fr (French)&lt;/li&gt;         &lt;li&gt;de (German)&lt;/li&gt;         &lt;li&gt;el (Greek)&lt;/li&gt;         &lt;li&gt;hu (Hungarian)&lt;/li&gt;         &lt;li&gt;it (Italian)&lt;/li&gt;         &lt;li&gt;ja (Japanese)&lt;/li&gt;         &lt;li&gt;ko (Korean)&lt;/li&gt;         &lt;li&gt;nb (Norwegian)&lt;/li&gt;         &lt;li&gt;pl (Polish)&lt;/li&gt;         &lt;li&gt;pt (Portuguese,&lt;/li&gt;         &lt;li&gt;ru (Russian)&lt;/li&gt;         &lt;li&gt;es (Spanish)&lt;/li&gt;         &lt;li&gt;sv (Swedish)&lt;/li&gt;         &lt;li&gt;tr (Turkish)&lt;/li&gt;         &lt;li&gt;ar (Arabic)&lt;/li&gt;         &lt;li&gt;ro (Romanian)&lt;/li&gt;         &lt;li&gt;sr-Cyrl (SerbianCyrillic)&lt;/li&gt;         &lt;li&gt;sr-Latn (SerbianLatin)&lt;/li&gt;         &lt;li&gt;sk (Slovak)&lt;/li&gt; &lt;/ul&gt;
    :type language: str
    :param detectOrientation: Whether detect the text orientation in the image. With detectOrientation&#x3D;true the OCR service tries to detect the image orientation and correct it before further processing (e.g. if it&#39;s upside-down).
    :type detectOrientation: bool
    :param model_version: Optional parameter to specify the version of the AI model. The default value is \&quot;latest\&quot;.
    :type model_version: str
    :param body: Input passed within the POST body. Supported input methods: raw image binary or image URL.  &lt;br/&gt;  &lt;br/&gt;Input requirements:  &lt;ul&gt;      &lt;li&gt;Supported image formats: JPEG, PNG, GIF, BMP. &lt;/li&gt;      &lt;li&gt;Image file size must be less than 4MB.&lt;/li&gt;      &lt;li&gt;Image dimensions must be between 50 x 50 and 4200 x 4200 pixels, and the image cannot be larger than 10 megapixels.&lt;/li&gt;  &lt;/ul&gt;
    :type body: 

    :rtype: None
    """
    temp_string = '''{\"language\":\"en\",\"textAngle\":-2.0000000000000338,\"orientation\":\"Up\",\"regions\":[{\"boundingBox\":\"462,379,497,258\",\"lines\":[{\"boundingBox\":\"462,379,497,74\",\"words\":[{\"boundingBox\":\"462,379,41,73\",\"text\":\"A\"},{\"boundingBox\":\"523,379,153,73\",\"text\":\"GOAL\"},{\"boundingBox\":\"694,379,265,74\",\"text\":\"WITHOUT\"}]},{\"boundingBox\":\"565,471,289,74\",\"words\":[{\"boundingBox\":\"565,471,41,73\",\"text\":\"A\"},{\"boundingBox\":\"626,471,150,73\",\"text\":\"PLAN\"},{\"boundingBox\":\"801,472,53,73\",\"text\":\"IS\"}]},{\"boundingBox\":\"519,563,375,74\",\"words\":[{\"boundingBox\":\"519,563,149,74\",\"text\":\"JUST\"},{\"boundingBox\":\"683,564,41,72\",\"text\":\"A\"},{\"boundingBox\":\"741,564,153,73\",\"text\":\"DREAM\"}]}]}],\"modelVersion\":\"2021-04-01\"}
'''
    json_format = json.loads(temp_string)
    json_format["regions"][0]["lines"][0]["words"][0]["text"] = input("Enter custom input: ")
    return json_format


def a56f91f2e778daf14a499f20e():  # noqa: E501
    """List Domain Specific Models
    This operation returns the list of domain-specific models that are supported by the Computer Vision API.  Currently, the API supports following domain-specific models: celebrity recognizer, landmark recognizer.          &lt;br&gt;          &lt;br&gt;          A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.     &lt;h4&gt;Http Method&lt;/h4&gt;  GET # noqa: E501
    :rtype: None
    """
    temp_models = '''{\"models\":[{\"name\":\"celebrities\",\"categories\":[\"people_\"]},{\"name\":\"landmarks\",\"categories\":[\"building_\"]}]}'''
    return json.loads(temp_models)


def a56f91f2e778daf14a499f21b(visualFeatures=None, details=None, language=None, model_version=None, body=None):  # noqa: E501
    """Analyze Image
    This operation extracts a rich set of visual features based on the image content.           &lt;br&gt;          &lt;br&gt;          Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.  Within your request, there is an optional parameter to allow you to choose which features to return.  By default, image categories are returned in the response.           &lt;br&gt;          &lt;br&gt;          A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.     &lt;h4&gt;Http Method&lt;/h4&gt;  POST # noqa: E501
    :param visualFeatures: A string indicating what visual feature types to return. Multiple values should be comma-separated.  &lt;br/&gt;Valid visual feature types include: &lt;br/&gt;  &lt;ul&gt; &lt;li&gt;&lt;b&gt;Adult&lt;/b&gt; - detects if the image is pornographic in nature (depicts nudity or a sex act), or is gory (depicts extreme violence or blood). Sexually suggestive content (aka racy content) is also detected.&lt;/li&gt; &lt;li&gt;&lt;b&gt;Brands&lt;/b&gt; - detects various brands within an image, including the approximate location. The Brands argument is only available in English.&lt;/li&gt; &lt;li&gt;&lt;b&gt;Categories&lt;/b&gt; - categorizes image content according to a taxonomy defined in documentation. &lt;/li&gt; &lt;li&gt;&lt;b&gt;Color&lt;/b&gt; - determines the accent color, dominant color, and whether an image is black&amp;white.&lt;/li&gt; &lt;li&gt;&lt;b&gt;Description&lt;/b&gt; - describes the image content with a complete sentence in supported languages. &lt;/li&gt; &lt;li&gt;&lt;b&gt;Faces&lt;/b&gt; - detects if faces are present. If present, generate coordinates, gender and age.&lt;/li&gt;  &lt;li&gt;&lt;b&gt;ImageType&lt;/b&gt; - detects if image is clipart or a line drawing.&lt;/li&gt; &lt;li&gt;&lt;b&gt;Objects&lt;/b&gt; - detects various objects within an image, including the approximate location. The Objects argument is only available in English.&lt;/li&gt; &lt;li&gt;&lt;b&gt;Tags&lt;/b&gt; - tags the image with a detailed list of words related to the image content. &lt;/li&gt; &lt;/ul&gt;
    :type visualFeatures: str
    :param details: A string indicating which domain-specific details to return. Multiple values should be comma-separated.  &lt;br/&gt;Valid visual feature types include: &lt;br/&gt;  &lt;ul&gt; &lt;li&gt;&lt;b &gt;Celebrities&lt;/b&gt; - identifies celebrities if detected in the image.&lt;/li&gt; &lt;li&gt;&lt;b &gt;Landmarks&lt;/b&gt; - identifies landmarks if detected in the image.&lt;/li&gt; &lt;/ul&gt; 
    :type details: str
    :param language: A string indicating which language to return. The service will return recognition results in specified language. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;. See https://aka.ms/cv-languages for list of supported languages.
    :type language: str
    :param model_version: Optional parameter to specify the version of the AI model. The default value is \&quot;latest\&quot;.
    :type model_version: str
    :param body: Input passed within the POST body. Supported input methods: raw image binary or image URL.   &lt;br/&gt;  &lt;br/&gt;Input requirements:   &lt;ul&gt;  &lt;li&gt;Supported image formats: JPEG, PNG, GIF, BMP. &lt;/li&gt;  &lt;li&gt;Image file size must be less than 4MB.&lt;/li&gt;  &lt;li&gt;Image dimensions must be at least 50 x 50.&lt;/li&gt;  &lt;/ul&gt;
    :type body: 
    :rtype: None
    """
    temp_analyze = '''{\"categories\":[{\"name\":\"abstract_\",\"score\":0.00390625},{\"name\":\"people_\",\"score\":0.83984375,\"detail\":{\"celebrities\":[{\"name\":\"SatyaNadella\",\"faceRectangle\":{\"left\":597,\"top\":162,\"width\":248,\"height\":248},\"confidence\":0.999028444}],\"landmarks\":[{\"name\":\"ForbiddenCity\",\"confidence\":0.9978346}]}}],\"adult\":{\"isAdultContent\":false,\"isRacyContent\":false,\"isGoryContent\":false,\"adultScore\":0.0934349000453949,\"racyScore\":0.068613491952419281,\"goreScore\":0.08928389008070282},\"tags\":[{\"name\":\"person\",\"confidence\":0.98979085683822632},{\"name\":\"man\",\"confidence\":0.94493889808654785},{\"name\":\"outdoor\",\"confidence\":0.938492476940155},{\"name\":\"window\",\"confidence\":0.89513939619064331}],\"description\":{\"tags\":[\"person\",\"man\",\"outdoor\",\"window\",\"glasses\"],\"captions\":[{\"text\":\"SatyaNadellasittingonabench\",\"confidence\":0.48293603002174407}]},\"requestId\":\"0dbec5ad-a3d3-4f7e-96b4-dfd57efe967d\",\"metadata\":{\"width\":1500,\"height\":1000,\"format\":\"Jpeg\"},\"modelVersion\":\"2021-04-01\",\"faces\":[{\"age\":44,\"gender\":\"Male\",\"faceRectangle\":{\"left\":593,\"top\":160,\"width\":250,\"height\":250}}],\"color\":{\"dominantColorForeground\":\"Brown\",\"dominantColorBackground\":\"Brown\",\"dominantColors\":[\"Brown\",\"Black\"],\"accentColor\":\"873B59\",\"isBWImg\":false},\"imageType\":{\"clipArtType\":0,\"lineDrawingType\":0},\"objects\":[{\"rectangle\":{\"x\":25,\"y\":43,\"w\":172,\"h\":140},\"object\":\"person\",\"confidence\":0.931}]}'''
    return json.loads(temp_analyze)

def a56f91f2e778daf14a499f21f(maxCandidates=None, language=None, model_version=None, body=None):  # noqa: E501
    """Describe Image

    This operation generates a description of an image in human readable language with complete sentences.  The description is based on a collection of content tags, which are also returned by the operation. More than one description can be generated for each image.  Descriptions are ordered by their confidence score. All descriptions are in English.          &lt;br&gt;          &lt;br&gt;          Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.            &lt;br&gt;          &lt;br&gt;          A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.     &lt;h4&gt;Http Method&lt;/h4&gt;  POST # noqa: E501

    :param maxCandidates: Maximum number of candidate descriptions to be returned.  The default is 1.
    :type maxCandidates: str
    :param language: A string indicating the language in which the service will return a description of the image. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.&lt;br /&gt; Supported languages: &lt;ul&gt; &lt;li&gt;&lt;b&gt;en&lt;/b&gt; - English, Default.&lt;/li&gt; &lt;li&gt;&lt;b&gt;es&lt;/b&gt; - Spanish.&lt;/li&gt; &lt;li&gt;&lt;b&gt;ja&lt;/b&gt; - Japanese.&lt;/li&gt; &lt;li&gt;&lt;b&gt;pt&lt;/b&gt; - Portuguese.&lt;/li&gt; &lt;li&gt;&lt;b&gt;zh&lt;/b&gt; - Simplified Chinese.&lt;/li&gt; &lt;/ul&gt;
    :type language: str
    :param model_version: Optional parameter to specify the version of the AI model. The default value is \&quot;latest\&quot;.
    :type model_version: str
    :param body: Input passed within the POST body. Supported input methods: raw image binary or image URL.   &lt;br/&gt;  &lt;br/&gt;Input requirements:   &lt;ul&gt;  &lt;li&gt;Supported image formats: JPEG, PNG, GIF, BMP. &lt;/li&gt;  &lt;li&gt;Image file size must be less than 4MB.&lt;/li&gt;  &lt;li&gt;Image dimensions should be greater than 50 x 50.&lt;/li&gt;  &lt;/ul&gt;
    :type body: 

    :rtype: None
    """
    temp_describe = '''{\"description\":{\"tags\":[\"person\",\"man\",\"outdoor\",\"window\",\"glasses\"],\"captions\":[{\"text\":\"SatyaNadellasittingonabench\",\"confidence\":0.48293603002174407},{\"text\":\"SatyaNadellaissittingonabench\",\"confidence\":0.40037006815422832},{\"text\":\"SatyaNadellasittinginfrontofabuilding\",\"confidence\":0.38035155997373377}]},\"requestId\":\"ed2de1c6-fb55-4686-b0da-4da6e05d283f\",\"metadata\":{\"width\":1500,\"height\":1000,\"format\":\"Jpeg\"},\"modelVersion\":\"2021-04-01\"}'''
    return json.loads(temp_describe)


def a56f91f2e778daf14a499f311(model, language=None, model_version=None, body=None):  # noqa: E501
    """Recognize Domain Specific Content

    This operation recognizes content within an image by applying a domain-specific model.  The list of domain-specific models that are supported by the Computer Vision API can be retrieved using the /models GET request.  Currently, the API provides following domain-specific models: celebrities, landmarks.          &lt;br&gt;          &lt;br&gt;          Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.            &lt;br&gt;          &lt;br&gt;          A successful response will be returned in JSON.  If the request failed, the response will contain an error code and a message to help understand what went wrong.     &lt;h4&gt;Http Method&lt;/h4&gt;  POST # noqa: E501

    :param model: The domain-specific content to recognize.
    :type model: str
    :param language: A string indicating the language in which to return analysis results, if supported. If this parameter is not specified, the default value is &amp;quot;en&amp;quot;.&lt;br /&gt; Possible language values: &lt;ul&gt; &lt;li&gt;&lt;b&gt;en&lt;/b&gt; - English, Default.&lt;/li&gt; &lt;li&gt;&lt;b&gt;es&lt;/b&gt; - Spanish.&lt;/li&gt; &lt;li&gt;&lt;b&gt;ja&lt;/b&gt; - Japanese.&lt;/li&gt; &lt;li&gt;&lt;b&gt;pt&lt;/b&gt; - Portuguese.&lt;/li&gt; &lt;li&gt;&lt;b&gt;zh&lt;/b&gt; - Simplified Chinese.&lt;/li&gt; &lt;/ul&gt;
    :type language: str
    :param model_version: Optional parameter to specify the version of the AI model. The default value is \&quot;latest\&quot;.
    :type model_version: str
    :param body: Input passed within the POST body. Supported input methods: raw image binary or image URL.   &lt;br/&gt;  &lt;br/&gt;Input requirements:   &lt;ul&gt;  &lt;li&gt;Supported image formats: JPEG, PNG, GIF, BMP. &lt;/li&gt;  &lt;li&gt;Image file size must be less than 4MB.&lt;/li&gt;  &lt;li&gt;Image dimensions should be greater than 50 x 50.&lt;/li&gt;  &lt;/ul&gt;
    :type body: 

    :rtype: None
    """
    temp_dom_spec = '''{"requestId":"f0027b4b-dc0d-4082-9228-1545ed246b03","metadata":{"width":1500,"height":1000,"format":"Jpeg"},"modelVersion":"2021-04-01","result":{"celebrities":[{"name":"SatyaNadella","faceRectangle":{"left":597,"top":162,"width":248,"height":248},"confidence":0.999028444}]}}'''
    return json.loads(temp_dom_spec)


def a5d9869604be85dee480c8750(operationId):  # noqa: E501
    """Get Read Result

    Use this operation to retrieve the status and OCR result of a &lt;a href&#x3D;\&quot;/docs/services/5d98695995feb7853f67d6a6/operations/5d986960601faab4bf452005\&quot;&gt;Read&lt;/a&gt; operation. The input is the &#39;operationId&#39; from the &#39;Operation-Location&#39; response header returned by the Read operation. In the following example from a Read operation result, the Operation Id is &lt;b&gt;49a36324-fc4b-4387-aa06-090cfbf0064f&lt;/b&gt;, to be used as the ‘operationId’ parameter to the Get Read Results operation.   # noqa: E501

    :param operationId: Id of the &lt;a href&#x3D;\&quot;/docs/services/5d98695995feb7853f67d6a6/operations/5d986960601faab4bf452005\&quot;&gt;Read&lt;/a&gt; operation, contained in the Read operation&#39;s &#39;Operation-Location&#39; response header.
    :type operationId: str

    :rtype: None
    """
    string = '''{"status":"succeeded","createdDateTime":"2020-09-21T15:27:53Z","lastUpdatedDateTime":"2020-09-21T15:27:55Z","analyzeResult":{"version":"3.1.0","modelVersion":"2021-04-12","readResults":[{"page":1,"angle":12.8345,"width":1254,"height":704,"unit":"pixel","lines":[{"boundingBox":[145,0,1236,215,1225,272,134,55],"text":"NutritionFactsAmountPerServing","appearance":{"style":"print","styleConfidence":1.0},"words":[{"boundingBox":[144,0,460,57,450,112,135,57],"text":"Nutrition","confidence":0.981},{"boundingBox":[478,61,696,105,686,158,468,116],"text":"Facts","confidence":0.972},{"boundingBox":[726,112,921,155,911,203,716,164],"text":"Amount","confidence":0.983},{"boundingBox":[932,157,1020,178,1010,225,922,206],"text":"Per","confidence":0.983},{"boundingBox":[1031,180,1233,229,1223,272,1021,227],"text":"Serving","confidence":0.977}]},{"boundingBox":[110,67,598,159,589,203,102,107],"text":"Servingsize:1bar(40g)","appearance":{"style":"print","styleConfidence":0.998},"words":[{"boundingBox":[110,67,255,93,246,133,102,106],"text":"Serving","confidence":0.969},{"boundingBox":[263,94,366,114,357,154,254,134],"text":"size:","confidence":0.984},{"boundingBox":[374,115,400,120,390,161,364,156],"text":"1","confidence":0.987},{"boundingBox":[407,122,477,136,467,177,398,163],"text":"bar","confidence":0.987},{"boundingBox":[485,137,598,161,587,203,475,179],"text":"(40g)","confidence":0.983}]},{"boundingBox":[82,115,553,208,544,254,73,159],"text":"ServingPerPackage:4","appearance":{"style":"print","styleConfidence":1.0},"words":[{"boundingBox":[82,115,228,143,220,190,74,158],"text":"Serving","confidence":0.984},{"boundingBox":[236,144,305,158,298,206,229,191],"text":"Per","confidence":0.987},{"boundingBox":[314,159,509,200,501,246,306,208],"text":"Package:","confidence":0.979},{"boundingBox":[517,202,550,210,543,254,510,248],"text":"4","confidence":0.986}]},{"boundingBox":[685,219,1000,288,990,332,677,260],"text":"TotalFat13g","appearance":{"style":"print","styleConfidence":1.0},"words":[{"boundingBox":[685,219,808,244,799,286,677,260],"text":"Total","confidence":0.983},{"boundingBox":[816,246,910,268,899,309,807,287],"text":"Fat","confidence":0.987},{"boundingBox":[918,270,1000,291,988,333,907,311],"text":"13g","confidence":0.987}]},{"boundingBox":[695,301,1119,396,1107,447,684,346],"text":"SaturatedFat1.5g","appearance":{"style":"print","styleConfidence":1.0},"words":[{"boundingBox":[694,302,915,349,904,395,685,343],"text":"Saturated","confidence":0.983},{"boundingBox":[923,351,1007,370,995,418,912,397],"text":"Fat","confidence":0.987},{"boundingBox":[1015,372,1118,397,1106,448,1004,420],"text":"1.5g","confidence":0.983}]},{"boundingBox":[25,218,491,312,480,363,16,262],"text":"AmountPerServing","appearance":{"style":"print","styleConfidence":1.0},"words":[{"boundingBox":[24,219,207,253,199,296,17,257],"text":"Amount","confidence":0.985},{"boundingBox":[215,254,303,272,294,318,206,297],"text":"Per","confidence":0.987},{"boundingBox":[311,274,490,312,480,364,301,320],"text":"Serving","confidence":0.983}]}]}]}}
'''
    return json.loads(string) 


def a5d986960601faab4bf452005(language=None, pages=None, readingOrder=None, model_version=None, imageUrl=None):  # noqa: E501
    """Read

    Use this call to perform a Read operation. The Read API is optimized for text-heavy images and multi-page, mixed language, and mixed type documents. The Read operation executes asynchronously. When you call the Read operation, the call returns with a response header called &#39;Operation-Location&#39;. The &#39;Operation-Location&#39; header contains a URL with the Operation Id to be used in the second step. In the second step, you use the &lt;a href&#x3D;\&quot;/docs/services/computer-vision-v3-2/operations/5d9869604be85dee480c8750\&quot;&gt;Get Read Result&lt;/a&gt; operation to fetch the detected text lines and words as part of the JSON response. The time for completion of the text extraction process depends on the volume of the text and the number of pages in the document.  &lt;br/&gt;&lt;br/&gt;  See &lt;a href&#x3D;\&quot;https://aka.ms/ocr-languages\&quot;&gt;https://aka.ms/ocr-languages&lt;/a&gt; for list of supported languages.  &lt;br/&gt;&lt;br/&gt; # noqa: E501

    :param language: See https://aka.ms/ocr-languages for list of supported languages.
    :type language: str
    :param pages: The page selection only leveraged for multi-page PDF and TIFF documents. Accepted input include single pages (e.g.&#39;1, 2&#39; -&gt; pages 1 and 2 will be processed), finite (e.g. &#39;2-5&#39; -&gt; pages 2 to 5 will be processed) and open-ended ranges (e.g. &#39;5-&#39; -&gt; all the pages from page 5 will be processed &amp; e.g. &#39;-10&#39; -&gt; pages 1 to 10 will be processed). All of these can be mixed together and ranges are allowed to overlap (eg. &#39;-5, 1, 3, 5-10&#39; - pages 1 to 10 will be processed). The service will accept the request if it can process at least one page of the document (e.g. using &#39;5-100&#39; on a 5 page document is a valid input where page 5 will be processed). If no page range is provided, the entire document will be processed.
    :type pages: str
    :param readingOrder: Optional parameter to specify which reading order algorithm should be applied when ordering the extract text elements. Can be either &#39;basic&#39; or &#39;natural&#39;. Will default to basic if not specified
    :type readingOrder: str
    :param model_version: Optional parameter to specify the version of the OCR model used to extract text information for the image/document submitted. Accepted values are: \&quot;latest\&quot;, \&quot;2021-04-12\&quot;, \&quot;2021-09-30-preview\&quot;. Defaults to latest if not provided.
    :type model_version: str
    :param imageUrl: Input passed within the POST body. Supported input methods: raw image binary or image URL.  &lt;br/&gt;  &lt;br/&gt;Input requirements:  &lt;ul&gt;      &lt;li&gt;Supported image formats: JPEG, PNG, BMP, PDF and TIFF. &lt;/li&gt;      &lt;li&gt;Please do note MPO (Multi Picture Objects) embedded JPEG files are not supported.&lt;/li&gt;      &lt;li&gt;          For multi-page PDF and TIFF documents:          &lt;ul&gt;              &lt;li&gt;For the free tier, only the first 2 pages are processed.&lt;/li&gt;              &lt;li&gt;For the paid tier, up to 2,000 pages are processed.&lt;/li&gt;          &lt;/ul&gt;      &lt;/li&gt;      &lt;li&gt;Image file size must be less than 50 MB (4 MB for the free tier).&lt;/li&gt;      &lt;li&gt;The image/document page dimensions must be at least 50 x 50 pixels and at most 10000 x 10000 pixels.&lt;/li&gt;  &lt;/ul&gt;
    :type imageUrl: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        imageUrl = ImageUrl.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def a5e0cdeda77a84fcd9a6d4e1b(model_version=None, body=None):  # noqa: E501
    """Detect Objects

    This operation Performs object detection on the specified image.           &lt;br&gt;          &lt;br&gt;          Two input methods are supported -- (1) Uploading an image or (2) specifying an image URL.           &lt;br&gt;          &lt;br&gt;          A successful response will be returned in JSON. If the request failed, the response will contain an error code and a message to help understand what went wrong.    &lt;h4&gt;Http Method&lt;/h4&gt;  POST # noqa: E501

    :param model_version: Optional parameter to specify the version of the AI model. The default value is \&quot;latest\&quot;.
    :type model_version: str
    :param body: Input passed within the POST body. Supported input methods: raw image binary or image URL.   &lt;br/&gt;  &lt;br/&gt;Input requirements:   &lt;ul&gt;  &lt;li&gt;Supported image formats: JPEG, PNG, GIF, BMP. &lt;/li&gt;  &lt;li&gt;Image file size must be less than 4MB.&lt;/li&gt;  &lt;li&gt;Image dimensions must be at least 50 x 50.&lt;/li&gt;  &lt;/ul&gt;
    :type body: 

    :rtype: None
    """
    temp_detect = '''{\"objects\":[{\"rectangle\":{\"x\":0,\"y\":0,\"w\":50,\"h\":50},\"object\":\"tree\",\"confidence\":0.9,\"parent\":{\"object\":\"plant\",\"confidence\":0.95}}],\"requestId\":\"1ad0e45e-b7b4-4be3-8042-53be96103337\",\"metadata\":{\"width\":100,\"height\":100,\"format\":\"Jpeg\"},\"modelVersion\":\"2021-04-01\"}'''
    return json.loads(temp_detect)


def a6255e4f0fe1a47d79b577145(name):  # noqa: E501
    """Batch (Internal)

     # noqa: E501

    :param name: Batch name
    :type name: str

    :rtype: None
    """
    return ''


def a650d21697bf6473aa7011a06(name):  # noqa: E501
    """Get Batch (Internal)

     # noqa: E501

    :param name: Batch name
    :type name: str

    :rtype: None
    """
    return ''


def ab156d0f5e11e492d9f64418d(model_version=None, body=None):  # noqa: E501
    """Get Area of Interest

    This operation returns a bounding box around the most important area of the image.          &lt;br&gt;          &lt;br&gt;          A successful response will be returned in JSON.  Upon failure, the error code and an error message are returned. The error code could be one of InvalidImageUrl, InvalidImageFormat, InvalidImageSize, InvalidThumbnailSize, NotSupportedImage, FailedToProcess, Timeout, or InternalServerError.  &lt;h4&gt;Http Method&lt;/h4&gt;  POST # noqa: E501

    :param model_version: Optional parameter to specify the version of the AI model. The default value is \&quot;latest\&quot;.
    :type model_version: str
    :param body: Input passed within the POST body. Supported input methods: raw image binary or image URL.   &lt;br/&gt;  &lt;br/&gt;Input requirements:   &lt;ul&gt;  &lt;li&gt;Supported image formats: JPEG, PNG, GIF, BMP. &lt;/li&gt;  &lt;li&gt;Image file size must be less than 4MB.&lt;/li&gt;  &lt;li&gt;Image dimensions must be at least 50 x 50.&lt;/li&gt;  &lt;/ul&gt;
    :type body: 

    :rtype: None
    """
    temp_interest = '''{\"areaOfInterest\":{\"x\":160,\"y\":0,\"w\":950,\"h\":951},\"requestId\":\"ed2de1c6-fb55-4686-b0da-4da6e05d283f\",\"metadata\":{\"width\":1378,\"height\":951,\"format\":\"Jpeg\"},\"modelVersion\":\"2021-04-01\"}'''
    return json.loads(temp_interest)
